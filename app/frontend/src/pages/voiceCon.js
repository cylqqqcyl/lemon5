import React, { useState, useEffect } from 'react';
import Head from 'next/head';
import { Layout as DashboardLayout } from 'src/layouts/dashboard/layout';
import io from 'socket.io-client';


// Connect to the socket.io server
// const socket = io('http://localhost:8080');

const Page = () => {

  return(
  <>
    <Head>
      <title>
        Lemon5 | 语音转换
      </title>
    </Head>
  </>
  );
};

Page.getLayout = (page) => (
  <DashboardLayout>
    {page}
  </DashboardLayout>
);

export default Page;
