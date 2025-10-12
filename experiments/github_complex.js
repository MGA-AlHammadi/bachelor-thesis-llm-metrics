/**
 * Complex number implementation (inspired by Complex.js)
 * https://github.com/infusion/Complex.js
 */

class Complex {
  constructor(re, im) {
    this.re = re;
    this.im = im;
  }

  add(other) {
    if (!(other instanceof Complex)) {
      throw new TypeError("Argument must be a Complex number");
    }
    return new Complex(this.re + other.re, this.im + other.im);
  }

  sub(other) {
    if (!(other instanceof Complex)) {
      throw new TypeError("Argument must be a Complex number");
    }
    return new Complex(this.re - other.re, this.im - other.im);
  }

  mul(other) {
    if (!(other instanceof Complex)) {
      throw new TypeError("Argument must be a Complex number");
    }
    const re = this.re * other.re - this.im * other.im;
    const im = this.re * other.im + this.im * other.re;
    return new Complex(re, im);
  }

  div(other) {
    if (!(other instanceof Complex)) {
      throw new TypeError("Argument must be a Complex number");
    }
    const denominator = other.re * other.re + other.im * other.im;
    if (denominator === 0) {
      throw new Error("Division by zero");
    }
    const re = (this.re * other.re + this.im * other.im) / denominator;
    const im = (this.im * other.re - this.re * other.im) / denominator;
    return new Complex(re, im);
  }

  abs() {
    return Math.sqrt(this.re * this.re + this.im * this.im);
  }

  conjugate() {
    return new Complex(this.re, -this.im);
  }

  toString() {
    const sign = this.im >= 0 ? "+" : "-";
    return `${this.re} ${sign} ${Math.abs(this.im)}i`;
  }
}

// Beispiel / Testcode
const a = new Complex(2, 3);
const b = new Complex(1, -4);

console.log("a:", a.toString());
console.log("b:", b.toString());
console.log("a + b =", a.add(b).toString());
console.log("a × b =", a.mul(b).toString());
console.log("|a| =", a.abs());
