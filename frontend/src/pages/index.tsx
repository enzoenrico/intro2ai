import { Textarea } from '@nextui-org/input'
import { Button } from '@nextui-org/button'
import { useState } from 'react'

import { useTheme } from '@/hooks/use-theme'
import { useAI } from '@/hooks/use-ai'

import DefaultLayout from '@/layouts/default'

export default function IndexPage () {
  useTheme('dark')

  const { data, isLoading, error } = useAI()

  const [userinp, setUserinp] = useState('')

  return (
    <DefaultLayout>
      <div className='w-full h-full flex flex-col items-center justify-around'>
        <div
          className='z-20 w-3/5 h-3/5 max-h-64 border border-blue-500 flex items-center justify-center p-5 transition-all text-wrap overflow-hidden rounded-2xl'
          style={
            userinp !== ''
              ? {
                  backdropFilter: 'blur(2px)',
                  boxShadow: '0 0 20px 8px rgba(0, 112, 243, 0.7)',
                  backgroundColor: 'rgba(0, 112, 243, 0.01)'
                }
              : {}
          }
        >
          {/* TODO: add isloading element */}
          <p className='silkscreen text-md'>hello world</p>
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
              onPress={() => {
                console.log(data)
              }}
            >
              Ask
            </Button>
          }
          maxRows={3}
          minRows={1}
          placeholder='ask away!'
          variant='underlined'
          onChange={e => {
            setUserinp(e.target.value)
          }}
        />
      </div>
    </DefaultLayout>
  )
}
