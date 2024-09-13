import { Link } from "@nextui-org/link";

import { Navbar } from "@/components/navbar";

export default function DefaultLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <div className="relative flex flex-col h-screen">
            <div className="relative h-screen w-full bg-slate-950">
                <div className="absolute bottom-0 left-0 right-0 top-0 bg-[linear-gradient(to_right,#002959_1px,transparent_1px),linear-gradient(to_bottom,#002959_1px,transparent_1px)] bg-[size:14px_24px] [mask-image:radial-gradient(ellipse_100%_60%_at_50%_10%,#000_10%,transparent_100%)]" />
                <main className="container mx-auto h-screen max-w-7xl px-6 flex-grow pt-16">
                    {children}
                </main>
                <footer className="w-full flex items-center justify-center py-3">
                    <Link
                        isExternal
                        className="flex items-center gap-1 text-current"
                        href="https://nextui-docs-v2.vercel.app?utm_source=next-pages-template"
                        title="nextui.org homepage"
                    >
                        <span className="text-default-600">Powered by</span>
                        <p className="text-primary">NextUI</p>
                    </Link>
                </footer>
            </div>
        </div>
    );
}
