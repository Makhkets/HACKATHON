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
                            <li className="active">
                                <a>
                                    <ion-icon name="grid" style={{fontSize: "25px"}}></ion-icon>
                                    <p color="red">Категория</p>
                                </a>
                            </li>
                            <li>
                                <a>
                                    <ion-icon name="book" style={{fontSize: "25px"}}></ion-icon>
                                    <p>Подборка</p>
                                </a>
                            </li>
                            <li>
                                <a>
                                    <ion-icon name="desktop" style={{fontSize: "25px"}}></ion-icon>
                                    <p>Журналы</p>
                                </a>
                            </li>
                            <li>
                                <a>
                                    <ion-icon name="bookmark" style={{fontSize: "25px"}}></ion-icon>
                                    <p>Товары</p>
                                </a>
                            </li>

                        </ul>
                    </div>
                    <div className="hr"></div>

                    <div className="two_puncts">
                        <ul>
                            <li>
                                <a href="https://t.me/mahamerz" style={{textDecoration: "none"}}>
                                    <ion-icon name="flash" style={{fontSize: "25px"}}></ion-icon>
                                    <p>Поддержка</p>
                                </a>
                            </li>
                            <li>
                                <a>
                                    <ion-icon name="moon" style={{fontSize: "23px"}}></ion-icon>
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