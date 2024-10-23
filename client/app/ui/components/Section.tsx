import React from "react";

interface Props {
  children: React.ReactNode;
  rounded?: boolean;
  backgroundColour?: "bg-cyan-300" | "bg-red-300";
}

export const Section: React.FC<Props> = ({
  children,
  rounded = false,
  backgroundColour = false,
}) => {
  return (
    <div className={`${backgroundColour} p-10 ${rounded && "rounded-2xl"}`}>
      {children}
    </div>
  );
};
