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
import "./styles/lp.css";

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
        window.location.href = "/";
        // console.log("Hi");
      })
    );
  };
  const chatRoom = () => {
    window.location.href = "/comments";
  };
  useEffect(() => {
    getCurrUser();
  }, []);

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
      <section id="hero">
        <div class="hero container">
          <div>
            <h1>
              Welcome <span></span>
            </h1>
            <h1>
              {user} <span></span>
            </h1>
          </div>
        </div>
      </section>
      <section id="services">
        <div class="services container">
          <div class="service-top">
            <h1 class="section-title">
              Facil<span>i</span>ties
            </h1>
            <p>
              Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ipsum
              deleniti maiores pariatur assumenda quas magni et, doloribus quod
              voluptate quasi molestiae magnam officiis dolorum, dolor provident
              atque molestias voluptatum explicabo!
            </p>
          </div>
          <div class="service-bottom">
            <div class="service-item">
              <h2>Web Design</h2>
              <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Corporis debitis rerum, magni voluptatem sed architecto placeat
                beatae tenetur officia quod
              </p>
            </div>
            <div class="service-item">
              <h2>Web Design</h2>
              <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Corporis debitis rerum, magni voluptatem sed architecto placeat
                beatae tenetur officia quod
              </p>
            </div>
            <div class="service-item">
              <h2>Web Design</h2>
              <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Corporis debitis rerum, magni voluptatem sed architecto placeat
                beatae tenetur officia quod
              </p>
            </div>
            <div class="service-item">
              <h2>Web Design</h2>
              <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Corporis debitis rerum, magni voluptatem sed architecto placeat
                beatae tenetur officia quod
              </p>
            </div>
          </div>
        </div>
      </section>
      <section id="about">
        <div class="about container">
          <div class="col-right">
            <h1 class="section-title">
              About <span>Us</span>
            </h1>
            <h2>Make the most out of your campus!</h2>
            <p>
              Campus Connect is a hub where students can interact with their
              Campus! It allows people to view nearby restaurants, chat with
              peers in their major, and share their profile with fellow
              students. Campus Connect allows students, new and old, to better
              connect with their classmates and find a good lunch within walking
              distance of their classes.
            </p>
          </div>
        </div>
      </section>
      <section id="contact">
        <div class="contact container">
          <div>
            <h1 class="section-title">
              Contact <span>info</span>
            </h1>
          </div>
          <div class="contact-items">
            <div class="contact-item">
              <div class="icon">
                <img src="https://img.icons8.com/bubbles/100/000000/phone.png" />
              </div>
              <div class="contact-info">
                <h1>Phone</h1>
                <h2>+1 234 123 1234</h2>
                <h2>+1 234 123 1234</h2>
              </div>
            </div>
            <div class="contact-item">
              <div class="icon">
                <img src="https://img.icons8.com/bubbles/100/000000/new-post.png" />
              </div>
              <div class="contact-info">
                <h1>Email</h1>
                <h2>info@gmail.com</h2>
                <h2>abcd@gmail.com</h2>
              </div>
            </div>
            <div class="contact-item">
              <div class="icon">
                <img src="https://img.icons8.com/bubbles/100/000000/map-marker.png" />
              </div>
              <div class="contact-info">
                <h1>Address</h1>
                <h2>Fatikchhari, Chittagong, Bangladesh</h2>
              </div>
            </div>
          </div>
        </div>
      </section>
    </body>
  );
}

// rfce
