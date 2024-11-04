import Link from "next/link";

interface Props {
  label: string;
  linkRef: string;
}

export const NavLink: React.FC<Props> = ({ label, linkRef }) => {
  return (
    <Link className="hover:opacity-45" href={linkRef}>
      {label}
    </Link>
  );
};
