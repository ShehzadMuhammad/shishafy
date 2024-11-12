import React from "react";

interface Props {
  children: React.ReactNode;
  rounded?: boolean;
  backgroundColour?:
    | "bg-cyan-300"
    | "bg-red-300"
    | "bg-fuchsia-400"
    | "bg-slate-300";
  header?: boolean;
  footer?: boolean;
}

export const Section: React.FC<Props> = ({
  children,
  rounded = false,
  backgroundColour = false,
  header = false,
  footer = false,
}) => {
  return (
    <div
      className={`${backgroundColour} ${
        header && "bg-gradient-to-tl from-fuchsia-500 via-red-200 to-amber-100"
      }  ${
        footer && "bg-gradient-to-tl from-violet-200 via-fuchsia-50 to-white"
      } p-10  ${rounded && "rounded-2xl"}`}
    >
      {children}
    </div>
  );
};
