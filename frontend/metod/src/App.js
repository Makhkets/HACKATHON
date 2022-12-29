import React, { Fragment, useState } from "react"
import { Routes, Route, Link } from 'react-router-dom'

import Layout from "./components/Layout";
import Index from "./pages/Index"

import "./css/style.css"
import "./css/main.css"

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