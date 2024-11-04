interface Props {
  children: React.ReactNode;
  gap?: "gap-2" | "gap-4" | "gap-6";
}

export const Row: React.FC<Props> = ({ children, gap }) => {
  return <div className={`flex flex-row flex-wrap ${gap}`}>{children}</div>;
};
