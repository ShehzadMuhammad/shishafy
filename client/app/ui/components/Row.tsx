import clsx from "clsx";
interface Props {
  children: React.ReactNode;
  gap?: "gap-2" | "gap-4" | "gap-6";
  className?: string;
}

export const Row: React.FC<Props> = ({ children, gap, className }) => {
  return (
    <div className={clsx("flex", "flex-row", gap, className)}>{children}</div>
  );
};
