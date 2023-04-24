terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 3.0"
    }
  }
}

provider "google" {
  project     = "playground-s-11-5da94b2d"
  region      = "us-central1"
}

resource "google_compute_instance" "gnsvm" {
  name         = "gnsvm"
  project      = "playground-s-11-5da94b2d"
  zone         = "us-central1-a"
  machine_type = "e2-micro"

  tags = ["ssh-external"]

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2004-lts"
    }
  }

  network_interface {
    network = "default"
    access_config {
      // Allocate a public IP
    }
  }

  metadata_startup_script = <<-EOT
    #!/bin/bash
    useradd -m gns
    echo "gns:Password@123" | chpasswd
    usermod -aG sudo gns
    sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
    systemctl restart sshd
  EOT

  service_account {
    scopes = [
      "cloud-platform",
    ]
  }
}

resource "google_compute_firewall" "allow_ssh_external" {
  name    = "allow-ssh-external"
  project = "playground-s-11-5da94b2d"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["ssh-external"]
}
