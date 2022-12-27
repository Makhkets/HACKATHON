import React from "react";
import { Outlet, useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

import Footer from "./subcomponents/Footer";
import Cap from "./subcomponents/Cap";
import { useState } from "react";
import { useEffect } from "react";


const Layout = () => {

    
    const [flag, setFlag] = useState(null)


    useEffect(() => {
        // const result = async () => {
        //     const data = await getUser()
        //     console.log(data.data)

    
        //     if (data.data) {
        //         setFlag(true)
        //         setUser(data.data)
        //     } else {
        //         setFlag(false)
        //     }
        // }
        // result()
        setFlag(true)
      }, []);


    if (flag === null) {
        // значит не весь компонент загрузился
    } else {
        return (
            <>
                <div className="container">
                    <main>
                        <Cap />
                        <Outlet />
                    </main>
                </div>
                <Footer />
            </>
        );
    }
};

export default Layout;