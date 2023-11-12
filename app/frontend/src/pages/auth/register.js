import React, {useState}from 'react';
import Head from 'next/head';
import NextLink from 'next/link';
import { useRouter } from 'next/navigation';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { Box, Button, Link, Stack, TextField, Typography } from '@mui/material';
import { useAuth } from 'src/hooks/use-auth';
import { Layout as AuthLayout } from 'src/layouts/auth/layout';
import { CustomSnackbar } from 'src/sections/message/custom-snackbar'; 

const Page = () => {
  const [snackbarConfig, setSnackbarConfig] = useState({ message: '', type: '' });
  const router = useRouter();
  const auth = useAuth();
  const formik = useFormik({
    initialValues: {
      email: '',
      name: '',
      password: '',
      submit: null
    },
    validationSchema: Yup.object({
      email: Yup
        .string()
        .email('必须为合法邮箱地址')
        .max(50)
        .required('需要输入邮箱'),
      name: Yup
        .string()
        .max(50)
        .required('需要输入用户名'),
      password: Yup
        .string()
        .max(80)
        .required('需要输入密码')
    }),
    onSubmit: async (values, helpers) => {
      setSnackbarConfig({ message: '', type: '' });
      try {
        await auth.signUp(values.email, values.name, values.password);
        setSnackbarConfig({ message: '注册成功', type: 'success' });
        setTimeout(() => {
        router.push('/auth/login');
        }
        , 500);
      } catch (err) {
        helpers.setStatus({ success: false });
        helpers.setErrors({ submit: err.message });
        helpers.setSubmitting(false);
        setSnackbarConfig({ message: err.message, type: 'error' });
      }
    }
  });

  return (
    <>
      <Head>
        <title>
        Lemon5 | 注册
        </title>
      </Head>
      <Box
        sx={{
          flex: '1 1 auto',
          alignItems: 'center',
          display: 'flex',
          justifyContent: 'center'
        }}
      >
        <Box
          sx={{
            maxWidth: 550,
            px: 3,
            py: '100px',
            width: '100%'
          }}
        >
          <div>
            <Stack
              spacing={1}
              sx={{ mb: 3 }}
            >
              <Typography variant="h4">
                注册
              </Typography>
              <Typography
                color="text.secondary"
                variant="body2"
              >
                已有账号?
                &nbsp;
                <Link
                  component={NextLink}
                  href="/auth/login"
                  underline="hover"
                  variant="subtitle2"
                >
                  登录
                </Link>
              </Typography>
            </Stack>
            <form
              noValidate
              onSubmit={formik.handleSubmit}
            >
              <Stack spacing={3}>
                <TextField
                  error={!!(formik.touched.name && formik.errors.name)}
                  fullWidth
                  helperText={formik.touched.name && formik.errors.name}
                  label="用户名"
                  name="name"
                  onBlur={formik.handleBlur}
                  onChange={formik.handleChange}
                  value={formik.values.name}
                />
                <TextField
                  error={!!(formik.touched.email && formik.errors.email)}
                  fullWidth
                  helperText={formik.touched.email && formik.errors.email}
                  label="邮箱"
                  name="email"
                  onBlur={formik.handleBlur}
                  onChange={formik.handleChange}
                  type="email"
                  value={formik.values.email}
                />
                <TextField
                  error={!!(formik.touched.password && formik.errors.password)}
                  fullWidth
                  helperText={formik.touched.password && formik.errors.password}
                  label="密码"
                  name="password"
                  onBlur={formik.handleBlur}
                  onChange={formik.handleChange}
                  type="password"
                  value={formik.values.password}
                />
              </Stack>
              <Button
                fullWidth
                size="large"
                sx={{ mt: 3 }}
                type="submit"
                variant="contained"
              >
                注册账号
              </Button>
            </form>
          </div>
        </Box>
      </Box>
      {snackbarConfig.message&&<CustomSnackbar message={snackbarConfig.message} type={snackbarConfig.type} />}
    </>
  );
};

Page.getLayout = (page) => (
  <AuthLayout>
    {page}
  </AuthLayout>
);

export default Page;
