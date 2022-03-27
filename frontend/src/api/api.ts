import axios, { AxiosInstance} from 'axios';
import {IUser} from "../models/IUser";

const backendURL = "https://api.github.com/"

const instance = (): AxiosInstance => axios.create({
    baseURL: backendURL,
});

export const userAPI = {

}
