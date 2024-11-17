import clsx from "clsx";
interface Props {
  children: React.ReactNode;
  className?: string;
  gap?: "gap-1" | "gap-2" | "gap-4" | "gap-6";
}

export const Column: React.FC<Props> = ({
  children,
  className,
  gap = null,
}) => {
  return (
    <div className={clsx("flex", "flex-col", gap, className)}>{children}</div>
  );
};
