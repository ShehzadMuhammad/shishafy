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
      <body className="p-2">
        <div>{children}</div>
      </body>
    </html>
  );
}
