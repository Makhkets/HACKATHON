import { Link } from "react-router-dom";
import { useState } from "react";
import { useEffect } from "react";



const Sidebar = (props) => {
    console.log(props)

    return (
        <>
            <div className="sidebar">
                <div className="main_column">
                    <div className="title">
                        <p>POWERBANK 2.0</p>
                    </div>
                    <div className="puncts">
                        <ul>
                            <li className={props.choice == "1" ? "active" : ""}>
                                <Link to="/">
                                    <ion-icon name="grid" style={{fontSize: "25px"}}></ion-icon>
                                    <p>Главная</p>
                                </Link>
                            </li>
                            <li className={props.choice == "2" ? "active" : ""}>
                                <Link to="information/null">
                                    <ion-icon name="book" style={{fontSize: "25px"}}></ion-icon>
                                    <p>Информация</p>
                                </Link>
                            </li>
                            <li className={props.choice == "3" ? "active" : ""}>
                                <Link to="/traffic">
                                    <ion-icon name="contrast-outline" style={{fontSize: "25px"}}></ion-icon>
                                    <p>Светофор</p>
                                </Link>
                            </li>
                            <li>
                                <a href="http://localhost/admin/" target="_blanks">
                                    <ion-icon name="desktop" style={{fontSize: "25px"}}></ion-icon>
                                    <p>Админка</p>
                                </a>
                            </li>

                        </ul>
                    </div>
                    <div className="hr"></div>

                    <div className="two_puncts">
                        <ul>
                            <li>
                                <a href="https://t.me/mahamerz" target="_blanks" style={{textDecoration: "none"}}>
                                    <ion-icon name="flash" style={{fontSize: "25px"}}></ion-icon>
                                    <p>Поддержка</p>
                                </a>
                            </li>
                            <li>
                                <a href="https://t.me/POWERBANK2023" target="_blanks">
                                    <ion-icon name="people" style={{fontSize: "25px"}}></ion-icon>
                                    <p>Команда</p>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </>
    );
};

export default Sidebar;