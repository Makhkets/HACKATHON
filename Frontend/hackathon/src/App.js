import React, { Fragment, useState } from "react"
import { Routes, Route, Link } from 'react-router-dom'

import Layout from "./components/Layout";
import Index from "./pages/Index"
// import Branch from "./pages/Branch";
// import Add from "./pages/Add"
// import Information from "./pages/Information"
// import Signup from "./pages/Signup";
// import Signin from "./pages/Signin";

// import { getUser } from "./actions/user";

// import "./css/style.css"
// import "./css/index.css"


// import Activate from "./pages/Activate";
// import PatientProfile from "./pages/PatientPage";
// import ActiveBranch from "./pages/ActiveBranch";
// import FindPage from "./pages/FindPage";
// import Visitor from "./pages/Visitor";
// import Personal from "./pages/Personal";
// import RequestDoctor from "./pages/RequestDoctor";


const App = () => {
  return (
      <Fragment>

          <Routes>
            <Route path="/" element={<Layout />} >
                <Route index element={<Index />} />
            </Route>        
          </Routes>

      </Fragment>
  );
}


export default App;