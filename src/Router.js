import { BrowserRouter, Switch, Route } from "react-router-dom";
import LandingPage from "./components/landingPage";
import Home from "./components/home";
import Comments from "./components/Comments";
import Profile from "./components/profile";
import Register from "./components/Register";
import Login from "./components/login";

const Router = () => {
  return (
    <div>
      <BrowserRouter>
        <Switch>
          <Route path="/comments">
            <Comments />
          </Route>
          <Route path="/home">
            <Home />
          </Route>
          <Route path="/profile">
            <Profile />
          </Route>
          <Route path="/register">
            <Register />
          </Route>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/">
            <LandingPage />
          </Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
};

export default Router;
