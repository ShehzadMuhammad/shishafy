import Logo from "@/app/public/shishafy-logo.svg";
import { NavLink } from "@/app/ui/components/NavLink";
import { AppBar, Box, Toolbar } from "@mui/material";
import Image from "next/image";
import Link from "next/link";

export const NavBar: React.FC = () => {
  return (
    <Box className="flex-grow">
      <AppBar color="transparent" position="static">
        <Toolbar className="flex justify-between">
          <Box display="flex" gap="12px">
            <Link href="/">
              <Image src={Logo} width={24} alt="Logo" />
            </Link>
            <NavLink label="Shishafy" linkRef="/" />
          </Box>

          <Box display="flex" gap="12px">
            <NavLink label="Order" linkRef="/order" />
            <NavLink label="Login" linkRef="/llogin" />
          </Box>
        </Toolbar>
      </AppBar>
    </Box>
  );
};
