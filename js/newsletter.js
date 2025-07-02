    const emailInput = document.getElementById("email");
    const newsletterBtn = document.getElementById("newsletter_btn");

  function esEmailValido(email) {
      const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return regex.test(email);
    }

  function obtenerCorreosGuardados() {
      const correos = localStorage.getItem("savedEmails");
      return correos ? JSON.parse(correos) : [];
    }

    function guardarCorreo(email) {
      const correos = obtenerCorreosGuardados();

      if (!correos.includes(email)) {
        correos.push(email);
        localStorage.setItem("savedEmails", JSON.stringify(correos));
        alert("✅ Correo guardado: " + email);
      } else {
        alert("⚠️ Este correo ya está registrado.");
      }
    }

    newsletterBtn.addEventListener("click", function () {
      const email = emailInput.value.trim();

      if (esEmailValido(email)) {
        guardarCorreo(email);
        emailInput.value = "";
      } else {
        alert("❌ Por favor, ingresa un correo válido.");
      }
    });