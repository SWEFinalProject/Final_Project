import React, { useState, useEffect } from "react";
import { Button, Text } from "./styles/button.style";
import {
  AppContainer,
  CollegeLogo,
  CollegeLogoOverlay,
} from "./styles/AppContainer.style";
import "./styles/lp.css";
import { Welcome, WelComeMessage } from "./styles/Welcome.style";

export default function Restaurant() {

  const [restaurantName, setRestaurantName] = useState("");
  const [user, setUser] = useState("");

  const search = async () => {
    
    const data = restaurantName;

    const responce = await fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(data),
    });

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
        window.location.href = "/";
        // console.log("Hi");
      })
    );
  };
  const chatRoom = () => {
    window.location.href = "/comments";
  };

  return (
    <body>
    <section id="header">
      <div class="header container">
        <div class="nav-bar">
          <div class="brand">
            <a href="#hero">
              <h1>
                <span>C</span>ampus <span>C</span>onnect
              </h1>
            </a>
          </div>
          <div class="nav-list">
            <div class="hamburger">
              <div class="bar"></div>
            </div>
            <ul>
              <li>
                <a href="#hero" data-after="Home">
                  Home
                </a>
              </li>
              <li>
                <a href="#about" data-after="About">
                  About
                </a>
              </li>
              <li>
                <a href="#services" data-after="Service">
                  Facilities
                </a>
              </li>
              <li>
                <a href="#contact" data-after="Contact">
                  Contact
                </a>
              </li>
              <li>
                <a onClick={logout}>Logout</a>
              </li>
              <li>
                <a onClick={chatRoom}>ChatRoom</a>
              </li>
              <li>
                <a href="#projects" data-after="Projects">
                  <i class="fa-solid fa-user"></i>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>
      <section>
        <div class="inputBx">
          <span>Restaurant Name</span>
          <input
            type="text"
            onChange={(e) => setRestaurantName(e.target.value)}
          ></input>
        </div>

        <div class="signin">
          <label>
            <input
              type="submit"
              value="Search"
              onClick={() => search()}
            />
          </label>
        </div>
      </section>
      <section id="contact">
        <div class="contact container">
          <div>
            <h1 class="section-title">
              <span>contributors</span>
            </h1>
          </div>
          <div class="contact-items">
            <div class="contact-item">
              <div class="icon">
                <img src="https://img.icons8.com/bubbles/100/000000/new-post.png" />
              </div>
              <div class="contact-info">
                <h1>Eliza Schuh</h1>
                <h2>info@gmail.com</h2>
              </div>
            </div>
            <div class="contact-item">
              <div class="icon">
                <img src="https://img.icons8.com/bubbles/100/000000/new-post.png" />
              </div>
              <div class="contact-info">
                <h1>Nur Haque</h1>
                <h2>info@gmail.com</h2>
              </div>
            </div>
            <div class="contact-item">
              <div class="icon">
                <img src="https://img.icons8.com/bubbles/100/000000/new-post.png" />
              </div>
              <div class="contact-info">
                <h1>Anish Ganga</h1>
                <h2>info@gmail.com</h2>
              </div>
            </div>
            <div class="contact-item">
              <div class="icon">
                <img src="https://img.icons8.com/bubbles/100/000000/new-post.png" />
              </div>
              <div class="contact-info">
                <h2>Alina Nemira</h2>
                <h2>info@gmail.com</h2>
              </div>
            </div>
          </div>
        </div>
      </section>
    </body>
  );
}
}