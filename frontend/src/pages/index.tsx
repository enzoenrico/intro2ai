import { Textarea } from '@nextui-org/input'
import { Button } from '@nextui-org/button'
import { useState } from 'react'

import { useTheme } from '@/hooks/use-theme'

import DefaultLayout from '@/layouts/default'
import { AIBox } from '@/components/AIBox'

export default function IndexPage () {
  useTheme('dark')
  const [userinp, setUserinp] = useState('')

  const [aiRepsonse, setAiResponse] = useState('')

  const handleQuestion = async () => {
    //test request

    // const response = await fetch('http://localhost:5000/test', {
    //   method: 'GET',
    //   headers: {
    //     'Content-Type': 'application/json'
    //   }
    // })

    const response = await fetch('http://localhost:5000/question/' + userinp, {
      method: 'GET'
    })
    const parsed = await response.json()

    // console.log(parsed)

    setAiResponse(parsed.message)
    setUserinp('')
  }

  return (
    <DefaultLayout>
      <div className='w-full h-full flex flex-col items-center justify-around'>
        <div className='z-20 w-full h-1/2 gap-5 flex flex-col items-center justify-center'>
          <h2 className='text-4xl font-bold'> your ai buddy </h2>
          <AIBox apiresponse={userinp || aiRepsonse} userinp={userinp} />
        </div>

        <Textarea
          className='max-w-[400px]'
          classNames={{
            input: 'no_scrollbar'
          }}
          endContent={
            <Button
              className='text-white h-min'
              color='primary'
              variant='bordered'
              onPress={handleQuestion}
            >
              Ask
            </Button>
          }
          maxRows={3}
          minRows={1}
          placeholder='ask away!'
          value={userinp}
          variant='underlined'
          onChange={e => {
            setUserinp(e.target.value)
          }}
        />
      </div>
    </DefaultLayout>
  )
}
