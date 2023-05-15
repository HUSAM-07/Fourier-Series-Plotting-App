import streamlit as st
import numpy as np
import matplotlib.pyplot 

st.title("Fourier Series Plotting App")
st.caption("Made by Mohammed Husamuddin, ID No.(2021A7PS0150U)")
st.divider()
# Define function
def f(x):
    return np.pi*np.ones_like(x)

# Define Fourier series coefficients
def fourier_coeffs(n):
    return np.array([0 if n%2==0 else 2*(-1)**((n-1)/2)/np.pi for n in range(1, n+1)])

# Define Fourier series approximation
def fourier_series(x, n):
    coeffs = fourier_coeffs(n)
    series = np.zeros_like(x)
    for i in range(n):
        series += coeffs[i]*np.sin((i+1)*x)
    return series

# Set up slider for number of terms in Fourier series
n_terms = st.sidebar.slider("Number of terms in Fourier series:", min_value=1, max_value=50, value=10, step=1)

# Create plot
fig, ax = plt.subplots()
x_vals = np.linspace(-np.pi, np.pi, num=1000)
ax.plot(x_vals, f(x_vals), label='f(x)')
ax.plot(x_vals, fourier_series(x_vals, n_terms), label=f'{n_terms} terms')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

# Add decorative elements
st.markdown('<style>.info {color: #1E88E5;}</style>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align: center; color: #1E88E5;">Fourier Series Demo</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: left; color: #E8F6EF;"> Question: </h2>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align: left; color: #E8F6EF;">  Plot the Fourier Series Graph for the function defined by = f(x) = 𝝅, -𝝅 ≤ x ≤ 𝝅 ; </h3>', unsafe_allow_html=True)
st.markdown('<p class="info">The Fourier series is a way of representing a periodic function as a sum of sinusoidal functions with different frequencies. This app demonstrates the Fourier series for the constant function f(x)=𝝅 over the interval [-\𝝅,\𝝅]. Use the slider to adjust the number of terms in the series and see how the Fourier series approximation improves with more terms.</p>', unsafe_allow_html=True)

# Display plot
st.pyplot(fig)







