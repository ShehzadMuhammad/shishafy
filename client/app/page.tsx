import ComputerPhone from "@/app/public/computer-phone.svg";
import DeliveryCar from "@/app/public/delivery-car.svg";
import DeliveryPerson from "@/app/public/delivery-person.svg";
import Logo from "@/app/public/shishafy-banner.png";
import Image from "next/image";
import { Column } from "./ui/components/Column";
import { InfoCard } from "./ui/components/InfoCard";
import { NavBar } from "./ui/components/Navbar";
import { Row } from "./ui/components/Row";
import { Section } from "./ui/components/Section";

export default function Home() {
  return (
    <>
      <NavBar />
      <Section isRounded isHeader>
        <div className="mt-28 mb-15">
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
          <p className="text-4xl">Who Are We?</p>
          <Row gap="gap-4">
            <div className="md:w-1/2 ">
              <p>
                Shishafy is a group of shisha lovers who enjoy the lounge as
                much as you do. We love the vibe, the flavours and the
                entertainment that it provides. At Shishafy we want to bring
                that lounge experience to the comfort of your homes. Sometimes
                you want to just enjoy a shisha at your house, without the
                surrounding noise. Control the music you want to play, control
                the entertainment and talk about whatever you want without
                worrying about whose listening in.
              </p>
            </div>
            <div className="flex justify-center mx-auto">
              <Image src={Logo} width={300} height={100} alt="Shishafy Logo" />
            </div>
          </Row>
        </Column>
      </Section>
      <Section>
        <Column gap="gap-2">
          <p className="text-4xl">How It Works</p>
          <Row gap="gap-4">
            <InfoCard
              title="Order"
              description="Give us a call or order from our website"
              imageSrc={ComputerPhone}
              imageAlt="Computer and Phone Logo"
            />
            <InfoCard
              title="Delivery"
              description="The Shisha will be delivered to your home"
              imageSrc={DeliveryCar}
              imageAlt="Delivery Car Logo"
            />
            <InfoCard
              title="SetUp"
              description="We will explain how to change the coals and make sure the shisha
            flavour is to your liking before leaving"
              imageSrc={DeliveryPerson}
              imageAlt="Delivery Person Logo"
            />
            <InfoCard
              title="End of Session"
              description="We come back at the agreed upon time for pickup"
              imageSrc={ComputerPhone}
              imageAlt="Computer and Phone Logo"
            />
          </Row>
        </Column>
      </Section>
      <Section isRounded isFooter>
        <Column>
          <p className="text-4xl">Contact Us</p>
          <p>Email: shishafy@gmail.com</p>
          <p>Phone: 647-702-2978</p>
        </Column>
      </Section>
    </>
  );
}
