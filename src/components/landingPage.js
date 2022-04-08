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
  return (
    <AppContainer>
      <CollegeLogoOverlay width="60em" height="60em" left="20%" bottom="0%">
        <CollegeLogo
          src="https://commkit.gsu.edu/files/2021/05/Flame_RGB.png"
          alt="GSU"
          width="20em"
          height="20em"
          left="30%"
          bottom="30%"
        ></CollegeLogo>
      </CollegeLogoOverlay>
      <Button
        left="43%"
        top="70%"
        color="red"
        width="20%"
        height="58px"
        color="#374057"
        onClick={TempAPI}
      >
        <Text color="white">Sign in with Microsoft</Text>
      </Button>
      <Welcome
        color="#374057"
        top="10px"
        left="35%"
        width="500px"
        height="80px"
      >
        <h1>
          <WelComeMessage>Welcome To Campus Connect!</WelComeMessage>
        </h1>
      </Welcome>
    </AppContainer>
  );
}

// rfce
