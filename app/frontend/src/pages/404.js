import React from 'react';
import Head from 'next/head';
import NextLink from 'next/link';
import ArrowLeftIcon from '@heroicons/react/24/solid/ArrowLeftIcon';
import { Box, Button, Container, SvgIcon, Typography } from '@mui/material';

const Page = () => (
  <>
    <Head>
      <title>
        Lemon5 | 404
      </title>
    </Head>
    <Box
      component="main"
      sx={{
        alignItems: 'center',
        display: 'flex',
        flexGrow: 1,
        minHeight: '100%'
      }}
    >
      <Container maxWidth="md">
        <Box
          sx={{
            alignItems: 'center',
            display: 'flex',
            flexDirection: 'column'
          }}
        >
          <Box
            sx={{
              mb: 3,
              textAlign: 'center'
            }}
          >
            <img
              alt="Under development"
              src="/assets/errors/error-404.png"
              style={{
                display: 'inline-block',
                maxWidth: '100%',
                width: 400
              }}
            />
          </Box>
          <Typography
            align="center"
            sx={{ mb: 3 }}
            variant="h3"
          >
            所访问的页面不存在
          </Typography>
          <Typography
            align="center"
            color="text.secondary"
            variant="body1"
          >
            404
          </Typography>
          <Button
            component={NextLink}
            href="/"
            startIcon={(
              <SvgIcon fontSize="small">
                <ArrowLeftIcon />
              </SvgIcon>
            )}
            sx={{ mt: 3 }}
            variant="contained"
          >
            返回
          </Button>
        </Box>
      </Container>
    </Box>
  </>
);

export default Page;
