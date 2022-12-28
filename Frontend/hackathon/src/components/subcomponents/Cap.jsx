import { Link, useNavigate } from "react-router-dom";
import { useState } from 'react';



const Cap = () => {
    
    return (
        <>
            <div className="cap__wrapper">
                <div className="cap">
                    <div className="container-4">
                           {/* onChange={e => setFindValue(e.target.value)} value={findValue} */}
                        <div className="groups">
                            <input type="search" id="search" placeholder="Поиск..." /> 
                            <button className="icon" style={{marginBottom: "2.5px"}}><i className="fa fa-search"></i></button>
                        </div>
                        <Link to="/enroll"><button style={{marginLeft: "3vh", height: "50px"}} className="beautifulButton">Админ Панель</button></Link>
                    </div>
                </div>



                <div className="nav">
                    <nav>
                        <ul>
                            <li><Link to="/signup">Регистрация</Link></li>
                            <li><Link to="/signin">Авторизация</Link></li>
                            <li><ion-icon name="notifications-outline" style={{fontSize: "30px", color: "rgb(68, 76, 226)", cursor: "pointer"}}></ion-icon></li>
                            <li><ion-icon name="bookmark-outline" style={{fontSize: "30px", color: "rgb(68, 76, 226)", cursor: "pointer"}}></ion-icon></li>
                            <li>
                                <div className="nav__img">
                                    <img src="https://www.meme-arsenal.com/memes/723c78e9be76eba2598c2d4c611f994c.jpg" alt="" />
                                </div>
                            </li>
                        </ul>
                    </nav>
                </div>
            </div>
        </>
    );
};

export default Cap;