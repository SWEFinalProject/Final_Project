import { BrowserRouter, Switch, Route } from "react-router-dom";
import LandingPage from "./components/landingPage";
import Home from "./components/home";
import Comments from "./components/Comments";

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
          <Route path="/">
            <LandingPage />
          </Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
};

export default Router;
