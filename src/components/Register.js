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
  const [alt_email, setAlt_email] = useState("");
  const authenticate = async () => {
    const data = {
      f_name,
      l_name,
      gsu_id,
      level,
      phone,
      password,
      primary_major,
      alt_email,
    };

    const response = await fetch("/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(data),
    });
    // Integrate verify page.
    console.dir(response.status);
    if (response.status == 401) {
      console.log("Register unsuccessful");
    } else if (response.status == 200) {
      window.location.href = "/login";
    } else {
      console.log("Register unsuccessful");
    }
  };
  return (
    <section>
      <div class="imgBx">
        <img
          src="https://sec.gsu.edu/files/2021/01/feature-image-ADM-APPLY-1.jpg"
          alt="image"
        />
      </div>
      <div class="contentBox">
        <div class="formBx">
          <h2>Login</h2>
          <form>
            <div class="inputBx">
              <span>First Name: </span>
              <input
                type="text"
                required
                onChange={(e) => setF_name(e.target.value)}
              ></input>
              <br />
              <br />
              <span>Last Name: </span>
              <input
                type="text"
                required
                onChange={(e) => setL_name(e.target.value)}
              ></input>

              <br />
              <br />

              <span>GSU ID: </span>
              <input
                type="text"
                required
                onChange={(e) => setGsu_id(e.target.value)}
              ></input>

              <br />
              <br />

              <span>Level: </span>
              <input
                type="text"
                required
                onChange={(e) => setLevel(e.target.value)}
              ></input>

              <br />
              <br />

              <span>Phone: </span>
              <input
                type="text"
                required
                onChange={(e) => setPhone(e.target.value)}
              ></input>

              <br />
              <br />

              <span>Primary Major: </span>
              <input
                type="text"
                required
                onChange={(e) => setPrimary_major(e.target.value)}
              ></input>

              <br />
              <br />

              <span>password: </span>
              <input
                type="password"
                required
                onChange={(e) => setPassword(e.target.value)}
              ></input>

              <br />
              <br />

              <span>Alternate Email: </span>
              <input
                type="text"
                required
                onChange={(e) => setAlt_email(e.target.value)}
              ></input>

              <br />
              <br />
            </div>

            <div class="signin">
              <label>
                <input
                  type="submit"
                  value="Sign in"
                  onClick={() => authenticate()}
                />
              </label>
            </div>
            <div class="signUp">
              <p>
                Dont have an account? <a href="/register">Sign up</a>
              </p>
            </div>
          </form>
        </div>
      </div>
    </section>
  );
}

export default Register;
