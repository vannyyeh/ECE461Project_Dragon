import styled from 'styled-components';

export const PageDiv = styled.div`
	font-size: 24px;
	text-align: center;
`;

export const Header1 = styled.div`
	display: flex;
	flex-direction: in-line;
	align-items: center;
	justify-content: center;
	margin-left; auto;
	margin-right: auto;
	text-align: center;
	font-family: 'Copperplate', 'Courier New', sans-serif;
	font-size: 30px;
	color: #663399;
`;

export const Header2 = styled.div`
	font-family: 'Monaco', 'Courier New', monospace;
	font-size: 22px;
	text-align: center;
`;

export const Wrapper = styled.div`
	background: #ffe4b5;
	margin: 12px auto;
	padding: 24px;
	border-radius: 20px;
	width: 60%;
`;

export const CheckInButton = styled.div`
	display: inline-block;
	padding: 12px 24px;
	background: linear-gradient(to bottom right, #e66465, #9198e5);
	color: white;
	border-radius: 15px;
	box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
	transition: all 0.3s ease;
	cursor: pointer;
`;

export const FormRegister = styled.div`
    display: flex;
    flex-direction: row;
    alignItems: center;
    marginTop: 20px;
    minWidth: 250px;
    padding: 10px 20px;
    gap: 20px;
    align-items: center;
    flex-wrap: wrap;
    justify-content: center;
}
`;

export const WrapperRegister = styled.div`
	background: #ffe4b5;
	display: flex;
	flex-direction: column;
	alignitems: center;
	margin: 25px auto;
	padding: 24px;
	border-radius: 20px;
	width: 60%;
`;

export const InputBoxContainer = styled.div`
	display: flex;
	align-items: center;
	justify-content: center;
`;

export const NavigationHeader = styled.div`
	display: flex;
	flex: center;
	flex-direction: in-line;
	align-items: center;
	justify-content: space-between;
	height: 50px;
	border-bottom: 3px solid red;
	width: 100%;
	margin-bottom: 25px;
`;

export const NavigationPage = styled.div`
	width: 120px;
	font-size: 35px;
	display: flex;
	justify-content: center;
	align-items: center;
	cursor: pointer;
`;
