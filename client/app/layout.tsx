import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Shishafy",
  description: "Order Shisha Delivered and prepared at your home",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body id="__next">
        <div>{children}</div>
      </body>
    </html>
  );
}
