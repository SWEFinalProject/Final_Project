import React from "react";
import { useState, useEffect } from "react";

function Register() {
  const [f_name, setF_name] = useState("");
  const [l_name, setL_name] = useState("");
  const [gsu_id, setGsu_id] = useState("");
  const [level, setLevel] = useState("");
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");
  const [primary_major, setPrimary_major] = useState("");
  const authenticate = async () => {
    const data = {
      f_name,
      l_name,
      gsu_id,
      level,
      phone,
      password,
      primary_major,
    };
    const responce = await fetch("/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(data),
    });
    console.dir(responce.status);
    if (responce.status == 401) {
      // window.location.href = "/login";
      console.log("Register unsuccessful");
    } else {
      console.log("Register Successful");
    }
  };
  return (
    <div>
      <h1>Register</h1>
      <form>
        <label>First Name: </label>
        <input
          type="text"
          required
          onChange={(e) => setF_name(e.target.value)}
        ></input>

        <br />
        <br />

        <label>Last Name: </label>
        <input
          type="text"
          required
          onChange={(e) => setL_name(e.target.value)}
        ></input>

        <br />
        <br />

        <label>GSU ID: </label>
        <input
          type="text"
          required
          onChange={(e) => setGsu_id(e.target.value)}
        ></input>

        <br />
        <br />

        <label>Level: </label>
        <input
          type="text"
          required
          onChange={(e) => setLevel(e.target.value)}
        ></input>

        <br />
        <br />

        <label>Phone: </label>
        <input
          type="text"
          required
          onChange={(e) => setPhone(e.target.value)}
        ></input>

        <br />
        <br />

        <label>Primary Major: </label>
        <input
          type="text"
          required
          onChange={(e) => setPrimary_major(e.target.value)}
        ></input>

        <br />
        <br />

        <label>password: </label>
        <input
          type="password"
          required
          onChange={(e) => setPassword(e.target.value)}
        ></input>

        <br />
        <br />

        <button type="button" onClick={() => authenticate()}>
          Register
        </button>
      </form>
    </div>
  );
}

export default Register;
