import React from "react";
import { useState } from "react";

function Register() {
  const [gsu_id, setGsu_id] = useState("");
  const [password, setPassword] = useState("");
  const [incGsuID, setIncGsuID] = useState("");
  const [incPass, setIncPass] = useState("");

  const authenticate = async () => {
    const data = {
      gsu_id,
      password,
    };

    const responce = await fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(data),
    });
    console.log(responce.status);
    if (responce.status === 404) {
      setIncGsuID("Incorrect username");
    } else if (responce.status === 401) {
      setIncPass("Incorrect Password");
    } else if (responce.status === 200) {
      window.location.href = "/home";
    } else {
      console.log("login unsuccessful");
    }
  };

  return (
    <div>
      <h1>Login</h1>
      <form>
        <label>GSU ID: </label>
        <input
          type="text"
          required
          onChange={(e) => setGsu_id(e.target.value)}
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
        <p>{incGsuID}</p>
        <p>{incPass}</p>
      </form>
    </div>
  );
}

export default Register;
