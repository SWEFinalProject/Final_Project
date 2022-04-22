import { React, useEffect, useState } from "react";
import { Button } from "./styles/button.style";
import {
  AppContainer,
  CollegeLogo,
  CollegeLogoOverlay,
} from "./styles/AppContainer.style";
import { Search } from "./styles/search.style";
import { Welcome, WelComeMessage } from "./styles/Welcome.style";
import Form from "react-bootstrap/Form";
import "bootstrap/dist/css/bootstrap.min.css";

export default function LandingPage() {
  const [user, setUser] = useState("");
  const navigate = () => {
    window.location.href = "/comments";
  };
  const getCurrUser = () => {
    fetch("/user").then((response) =>
      response.json().then((data) => {
        setUser(data);
      })
    );
  };
  const logout = () => {
    fetch("/logout").then((response) =>
      response.json().then((data) => {
        console.log(data);
      })
    );
  };
  useEffect(() => {
    getCurrUser();
  }, []);
  return (
    <AppContainer>
      <div className="search">
        <Button
          left="10px"
          top="10px"
          color="red"
          width="56px"
          height="58px"
          onClick={navigate}
        >
          options
        </Button>
        <h2>Welcome back {user}</h2>
        <Button
          left="90%"
          top="10px"
          color="red"
          onClick={() => {
            window.location.href = "/profile";
          }}
        >
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png"
            alt="LoginLogo"
            width={56}
            height={58}
          />
        </Button>
        <Search>
          <input type="text" />
          <input type="button" value="search" />
        </Search>
      </div>
      <CollegeLogoOverlay width="60em" height="60em" left="45%" bottom="20%">
        <CollegeLogo
          src="https://commkit.gsu.edu/files/2021/05/Flame_RGB.png"
          alt="GSU"
          width="20em"
          height="20em"
          left="30%"
          bottom="30%"
        ></CollegeLogo>
      </CollegeLogoOverlay>
      <Welcome
        color="#374057"
        top="500px"
        left="10px"
        width="800px"
        height="200px"
      >
        <h1>
          <WelComeMessage>Welcome To Campus Connect!</WelComeMessage>
        </h1>
        <button onClick={logout}>Logout</button>
        <h1>
          <WelComeMessage>Make the most out of your campus!</WelComeMessage>
        </h1>
      </Welcome>
    </AppContainer>
  );
}

// rfce
