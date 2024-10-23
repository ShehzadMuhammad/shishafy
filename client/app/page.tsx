import { Card } from "./ui/components/Card";
import { Column } from "./ui/components/Column";
import { NavBar } from "./ui/components/Navbar";
import { Section } from "./ui/components/Section";

export default function Home() {
  return (
    <>
      <Section rounded backgroundColour="bg-cyan-300">
        <NavBar />
        <div className="my-28">
          <Column gap="gap-2">
            <p className="text-7xl">Make Your Home The Lounge.</p>
            <p>
              Shishafy provides that shisha lounge experience straight to your
              home. You control the music, you control the entertainment
            </p>
          </Column>
        </div>
      </Section>
      <Section>
        <Column gap="gap-2">
          <p className="text-4xl">How It Works</p>
          <div className="flex gap-2 mt-6">
            <Card
              title="Order"
              description="Give us a call or order from our website"
              image="image"
            />
            <Card
              title="Delivery"
              description="The Shisha will be delivered to your home"
              image="image"
            />
            <Card
              title="SetUp"
              description="We will explain how to change the coals and make sure the shisha
            flavour is to your liking before leaving"
              image="image"
            />
            <Card
              title="End of Session"
              description="We come back at the agreed upon time for pickup"
              image="image"
            />
          </div>
        </Column>
      </Section>
      <Section rounded backgroundColour="bg-red-300">
        <Column>
          <p className="text-4xl">Contact Us</p>
          <p>Email: shishafy@gmail.com</p>
          <p>Phone: 647-702-2978</p>
        </Column>
      </Section>
    </>
  );
}
