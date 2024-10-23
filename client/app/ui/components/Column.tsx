interface Props {
  children: React.ReactNode;
  gap?: "gap-2" | "gap-4" | "gap-6";
}

export const Column: React.FC<Props> = ({ children, gap = null }) => {
  return <div className={`flex flex-col ${gap}`}>{children}</div>;
};
