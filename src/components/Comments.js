import { React, useState, useEffect } from "react";
import { Comment, Groups, GroupComment } from "./styles/comments.style";
import { GroupTab, Labels } from "./styles/GroupTab.style";
import { CommentBox } from "./styles/commentBox.style";

function Comments() {
  const [state, setState] = useState("");
  const [comment, setCurrentComment] = useState("");
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
        <h3>{comment}</h3>
        <CommentBox action="">
          <input
            type="text"
            required
            onChange={(e) => setCurrentComment(e.target.value)}
          ></input>
          <input type="submit" />
        </CommentBox>
      </GroupComment>
    </Comment>
  );
}
export default Comments;
