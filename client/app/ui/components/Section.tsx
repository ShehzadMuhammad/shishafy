import clsx from "clsx";
import React from "react";
interface Props {
  children: React.ReactNode;
  className?: string;
  isRounded?: boolean;
  isHeader?: boolean;
  isFooter?: boolean;
}

export const Section: React.FC<Props> = ({
  children,
  className,
  isRounded = false,
  isHeader = false,
  isFooter = false,
}) => {
  return (
    <div
      className={clsx(
        "flex",
        "flex-col",
        isHeader &&
          "bg-gradient-to-tl from-fuchsia-500 via-red-200 to-amber-100",
        isFooter && "bg-gradient-to-tl from-violet-200 via-fuchsia-50 to-white",
        "p-10",
        isRounded && "rounded-2xl",
        className
      )}
    >
      {children}
    </div>
  );
};
