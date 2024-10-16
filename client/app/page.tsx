import { NavBar } from "./ui/components/Navbar";
import { Section } from "./ui/components/Section";

export default function Home() {
  return (
    <Section rounded backgroundColour>
      <div>
        <NavBar />
      </div>
      <div className="my-28">
        <div className="flex flex-col gap-2">
          <p className="text-5xl">Make Your Home The Lounge.</p>
          <p>
            Shishafy provides that shisha lounge experience straight to your
            home. You control the music, you control the entertainment
          </p>
        </div>
      </div>
    </Section>
  );
}
