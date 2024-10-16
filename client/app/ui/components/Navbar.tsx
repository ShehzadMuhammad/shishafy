export const NavBar: React.FC = () => {
  return (
    <div className="flex justify-between max-auto px-4 py-6 border-t-2 border-b-2 border-gray-800 ">
      <div className="cursor-pointer">
        <p className="text-lg">Shishafy</p>
      </div>
      <div className="flex gap-4">
        <p className="text-lg hover:opacity-45 cursor-pointer">Order</p>
        <p className="text-lg hover:opacity-45 cursor-pointer">Login</p>
      </div>
    </div>
  );
};
