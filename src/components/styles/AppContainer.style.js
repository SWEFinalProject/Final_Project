import styled from "styled-components";

export const AppContainer = styled.div`
  padding: 10px;
  width: 100vw;
  height: 50vw;
  background-image: url("https://blog.realmanage.com/hubfs/AdobeStock_316839352.jpeg");
  background-size: 100vw;
`;

export const CollegeLogoOverlay = styled.div`
  position: absolute;
  width: ${(props) => props.width};
  height: ${(props) => props.height};
  left: ${(props) => props.left};
  bottom: ${(props) => props.bottom};
  background-color: #97caeb;
  border-radius: 50%;
`;

export const CollegeLogo = styled.img`
  position: absolute;
  width: ${(props) => props.width};
  height: ${(props) => props.height};
  left: ${(props) => props.left};
  bottom: ${(props) => props.bottom};
`;
