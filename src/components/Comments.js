import { React, useState, useEffect } from "react";
import { Comment, Groups, GroupComment } from "./styles/comments.style";
import { GroupTab, Labels } from "./styles/GroupTab.style";

function Comments() {
  const [state, setState] = useState("");
  function fetchAPI() {
    fetch("/api")
      .then((response) => {
        if (response.status == 200) {
          return response.json();
        }
      })
      .then((data) => console.log(data))
      .then((error) => console.log(error));
  }
  useEffect(() => {
    fetchAPI();
  }, []);
  return (
    <Comment>
      <Groups>
        <GroupTab top="10px" color="white">
          <Labels>CSC 4530</Labels>
        </GroupTab>
        <GroupTab top="10px" color="white">
          <Labels>Rels 1000</Labels>
        </GroupTab>
        <GroupTab top="10px" color="white">
          <Labels>CSC 4230</Labels>
        </GroupTab>
        <GroupTab top="10px" color="white">
          <Labels>CSC 4130</Labels>
        </GroupTab>
        <GroupTab top="10px" color="white">
          <Labels>CSC 4030</Labels>
        </GroupTab>
      </Groups>

      <GroupComment>
        <form action="">
          <input type="text" />
          <input type="submit" />
        </form>
      </GroupComment>
    </Comment>
  );
}
export default Comments;
