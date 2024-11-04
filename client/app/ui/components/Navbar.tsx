import Link from "next/link";
import { NavLink } from "@/app/ui/components/NavLink";
import Logo from "@/app/public/shishafy-logo.svg";
import Image from "next/image";
import { Row } from "@/app/ui/components/Row";

export const NavBar: React.FC = () => {
  return (
    <div className="flex text-lg justify-between max-auto px-4 py-6 border-t border-b border-gray-800 ">
      <Link href="/">
        <Row gap="gap-2">
          <Image src={Logo} width={20} alt="Logo" />
          Shishafy
        </Row>
      </Link>
      <div className="flex gap-4">
        <NavLink label="Order" linkRef="/order" />
        <NavLink label="Login" linkRef="/llogin" />
      </div>
    </div>
  );
};
