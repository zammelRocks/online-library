import {Navigate} from 'react-router-dom';
import {jwtDecode} from 'jwt-decode';
import api from '../api';
import { REFRESH_TOKEN,ACCESS_TOKEN } from '../constants';
import {useState, useEffect } from 'react';

function ProtectedRoute({children}) {
    
    const [isAuthorized, setIsAuthorized] = useState(null);
    
    useEffect(() => {
        const checkAuth = async () => {
            try {
                await auth();
            } catch (error) {
                setIsAuthorized(false);
            }
        };

        checkAuth();
    }, []);


    const refreshToken = async () => {
        const refreshToken = localStorage.getItem(REFRESH_TOKEN);
        try {

            const response = await api.post('api/token/refresh/', {
                refreshToken,
            });
            if (response.status === 200){
                localStorage.setItem(ACCESS_TOKEN, response.data.accessToken);
                setIsAuthorized(true);
            }else{
                setIsAuthorized(false);
            }
        } catch (error) {

            console.log(error);
            setIsAuthorized(false);
        }


    } 

    const auth = async () => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (!token) {
            setIsAuthorized(false);
            return;
        }
        const decodedToken = jwtDecode(token);
        const tokenExpirationTime = decodedToken.exp;
        const currentTime = Date.now() / 1000;
        if (tokenExpirationTime < currentTime) {
            await refreshToken();
        } else {
            setIsAuthorized(true);
        }
        
    } 
    if (isAuthorized === null) {

        return <div>Loading...</div>;
    }
    return isAuthorized ? children : <Navigate to="/login" />;
    

}
export default ProtectedRoute;