export const LinkedInApi = {
  clientId: import.meta.env.VITE_CLIENT_ID,
  redirectUrl: "http://localhost:5173/",
  // redirectUrl: "https://reva-client-tenaris.azurewebsites.net/",
  oauthUrl:
    "https://www.linkedin.com/oauth/v2/authorization?response_type=code",
  scope: "r_liteprofile%20r_emailaddress",
  state: import.meta.env.VITE_STATE,
};

export const NodeServer = {
  baseURL: "http://localhost:5000",
  getUserCredentials: "/auth",
};
