import React from "react";
import { Button, Text } from "./styles/button.style";
import {
  AppContainer,
  CollegeLogo,
  CollegeLogoOverlay,
} from "./styles/AppContainer.style";
import { Welcome, WelComeMessage } from "./styles/Welcome.style";

export default function landingPage() {
  const TempAPI = () => {
    window.location.href = "/home";
  };
  const Register = () => {
    window.location.href = "/register";
  };
  return (
    <AppContainer>
      <CollegeLogoOverlay width="60em" height="60em" left="30%" bottom="0%">
        <CollegeLogo
          src="https://commkit.gsu.edu/files/2021/05/Flame_RGB.png"
          alt="GSU"
          width="20em"
          height="20em"
          left="35%"
          bottom="35%"
        ></CollegeLogo>
      </CollegeLogoOverlay>
      <Button
        left="48%"
        top="80%"
        color="red"
        width="20%"
        height="58px"
        color="#374057"
        onClick={Register}
      >
        <Text color="white">Sign in with Microsoft</Text>
      </Button>
      <Welcome
        color="#374057"
        top="10px"
        left="38%"
        width="600px"
        height="100px"
      >
        <h1>
          <WelComeMessage>Welcome To Campus Connect!</WelComeMessage>
        </h1>
      </Welcome>
    </AppContainer>
  );
}

// rfce
