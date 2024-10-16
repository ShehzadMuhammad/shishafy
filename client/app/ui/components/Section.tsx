import React from "react";

interface Props {
  children: React.ReactNode;
  rounded?: boolean;
  backgroundColour?: boolean;
}

export const Section: React.FC<Props> = ({
  children,
  rounded = false,
  backgroundColour = false,
}) => {
  return (
    <div
      className={`${backgroundColour && "bg-cyan-300"} p-10 ${
        rounded && "rounded-2xl"
      }`}
    >
      {children}
    </div>
  );
};
