import React, { Fragment, useState } from "react"
import { Routes, Route, Link } from 'react-router-dom'

import Layout from "./components/Layout";
import Index from "./pages/Index"

import "./css/style.css"
import "./css/main.css"

import Infromation from "./pages/Information";
import Admin from "./pages/TrafficLight";
import TrafficLight from "./pages/TrafficLight";

const App = () => {
  return (
      <Fragment>

          <Routes>
            <Route path="/" element={<Layout />} >
                <Route index element={<Index />} />
                <Route path="/information/:id" element={<Infromation />} />
                <Route path="/traffic" element={<TrafficLight />} />
            </Route>        
          </Routes>

      </Fragment>
  );
}


export default App; 