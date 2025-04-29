import { Link as MuiLink } from "@mui/material";
import Link from "next/link";

interface Props {
  label: string;
  linkRef: string;
}

export const NavLink: React.FC<Props> = ({ label, linkRef }) => {
  return (
    <MuiLink
      component={Link}
      href={linkRef}
      color="inherit"
      variant="h5"
      underline="none"
      className="hover:opacity-45"
    >
      {label}
    </MuiLink>
  );
};
