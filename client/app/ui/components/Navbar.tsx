import Logo from "@/app/public/shishafy-logo.svg";
import { NavLink } from "@/app/ui/components/NavLink";
import { AppBar, Box, Container, Toolbar } from "@mui/material";
import Image from "next/image";
import Link from "next/link";

export const NavBar: React.FC = () => {
  return (
    <AppBar position="fixed" className="bg-transparent shadow-none mt-4">
      <Container maxWidth="lg">
        <Toolbar className="flex items-center justify-between rounded-xl backdrop-blur-md border border-gray-200 bg-white/40 shadow-md px-3 py-2">
          <Box display="flex" gap="12px" color="black">
            <Link href="/">
              <Image src={Logo} width={24} alt="Logo" />
            </Link>
            <NavLink label="Shishafy" linkRef="/" />
          </Box>

          <Box display="flex" gap="12px">
            <NavLink label="Order" color="black" linkRef="/order" />
            <NavLink label="Login" color="black" linkRef="/llogin" />
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
};
