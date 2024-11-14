import { Column } from "@/app/ui/components/Column";
import { TextField } from "@/app/ui/components/TextField";
import { Row } from "@/app/ui/components/Row";

export const PersonalInfoStep: React.FC = () => {
  return (
    <Column gap="gap-4">
      <span className="text-lg">Enter Your Personal Information</span>
      <Row gap="gap-2">
        <TextField
          name="firstName"
          label="First Name"
          placeholder="Enter Your First Name"
        />
        <TextField
          name="lastName"
          label="Last Name"
          placeholder="Enter Your Last Name"
        />
      </Row>
      <Row gap="gap-2">
        <TextField
          name="Street Address"
          label="Stress Address"
          placeholder="Enter Your Street Address"
        />
        <TextField name="City" label="City" placeholder="Enter Your City" />
        <TextField
          name="Province"
          label="Province"
          placeholder="Enter Your Province"
        />
        <TextField
          name="Postal Code"
          label="Postal Code"
          placeholder="Enter Your Postal Code"
        />
      </Row>
    </Column>
  );
};
