import matplotlib.pyplot as plt


def reservoir_dict_to_str(input):
    """
    Convert an integer key to its corresponding string representation.

    Args:
        input (int): The integer key to be converted. Expected values are:
                     0 - "Timesteps"
                     1 - "Input Current"
                     2 - "Membrane Potential"
                     3 - "Spikes"

    Returns:
        str: The string representation corresponding to the input integer key.

    Raises:
        KeyError: If the input integer key is not found in the dictionary.
    """
    int_to_str = {
        0: "Timesteps",
        1: "Input Current",
        2: "Membrane Potential",
        3: "Spikes",
    }
    return int_to_str[input]


def reservoir_dict_to_int(input):
    """
    Converts a string key representing a reservoir property to its corresponding integer value.

    Args:
        input (str): The string key representing the reservoir property.
                     Expected values are "Timesteps", "Input Current", "Membrane Potential", or "Spikes".

    Returns:
        int: The integer value corresponding to the input string key.

    Raises:
        KeyError: If the input string key is not found in the predefined dictionary.
    """
    str_to_int = {
        "Timesteps": 0,
        "Input Current": 1,
        "Membrane Potential": 2,
        "Spikes": 3,
    }
    return str_to_int[input]


def plot_reservoir_data(x_train, y_train, reservoir_input_feature, reservoir_target):
    """
    Plots the reservoir input and target data for the first 50 samples.

    Parameters:
    x_train (array-like): The input data to the reservoir.
    y_train (array-like): The target data for the reservoir.
    reservoir_input_feature (str): The label for the reservoir input feature.
    reservoir_target (str): The label for the reservoir target.

    Returns:
    None
    """
    plt.plot(x_train[:50], label=f"Reservoir input: {reservoir_input_feature}")
    plt.plot(y_train[:50], label=f"Reservoir target: {reservoir_target}")
    plt.legend()
    plt.show()


def plot_reservoir_activations(reservoir_states):
    """
    Plots the activations of the first 20 reservoir neurons over time.

    Parameters:
    reservoir_states (numpy.ndarray): A 2D array where each row represents the state of the reservoir at a given timestep,
                                      and each column represents a different neuron in the reservoir.

    Returns:
    None
    """
    plt.figure(figsize=(10, 3))
    plt.title("Activation of 20 reservoir neurons.")
    plt.ylabel("Reservoir activations")
    plt.xlabel("Timesteps")
    plt.plot(reservoir_states[:, :20])
    plt.show()


def plot_reservoir_predictions(
    x_train, y_train, y_pred, reservoir_input_feature, reservoir_target
):
    """
    Plots the reservoir predictions against the actual data.

    Parameters:
    x_train (array-like): The input data used for training the reservoir.
    y_train (array-like): The actual target data.
    y_pred (array-like): The predicted target data from the reservoir.
    reservoir_input_feature (str): The name of the feature used as input to the reservoir.
    reservoir_target (str): The name of the target variable being predicted.

    Returns:
    None
    """
    plt.figure(figsize=(10, 3))
    plt.title("Comparing real data with the reservoirs prediction.")
    plt.xlabel("Timesteps")
    plt.plot(
        x_train[:70], label=f"Reservoir input: {reservoir_input_feature}", color="green"
    )
    plt.plot(y_pred, label=f"Predicted {reservoir_target}", color="blue")
    plt.plot(y_train[:70], label=f"Actual {reservoir_target}", color="red")
    plt.legend()
    plt.show()


def plot_results(results, param_sets):
    """
    Plots the input current and membrane potential for given simulation results.

    Parameters:
    results (dict): A dictionary where keys are labels and values are tuples containing:
                    - time (array-like): Time steps of the simulation.
                    - input_current (array-like): Input current values over time.
                    - membrane_potential (array-like): Membrane potential values over time.
                    - spikes (array-like): Boolean array indicating spike events.
    param_sets (dict): A dictionary where keys are labels and values are objects containing:
                       - v_threshold (float): Voltage threshold for spiking.
                       
    Returns:
    None
    """

    num_sets = len(results)
    fig, axs = plt.subplots(num_sets, 2, figsize=(10, 3 * num_sets))

    # Handle single plot case
    if num_sets == 1:
        axs1 = axs[0]
        axs2 = axs[1]
        for i, (label, (time, input_current, membrane_potential, spikes)) in enumerate(
            results.items()
        ):
            # Input Current plot
            axs1.set_title(f"{label} - Input Current")
            axs1.plot(time, input_current)
            axs1.set_xlabel("Timesteps")
            axs1.set_ylabel("Current")

            # Membrane Potential plot
            axs2.set_title(f"{label} - Membrane Potential")
            axs2.plot(time, membrane_potential)
            axs2.axhline(
                y=param_sets[label].v_threshold,
                color="r",
                linestyle="--",
                label="Threshold",
            )
            axs2.set_xlabel("Timesteps")
            axs2.set_ylabel("Voltage")
            axs2.legend()

            # Add spike indicators
            spike_times = time[spikes.bool()]
            axs2.vlines(
                spike_times,
                axs2.get_ylim()[0],
                axs2.get_ylim()[1],
                color="r",
                linewidth=0.5,
                alpha=0.5,
            )

    else:
        for i, (label, (time, input_current, membrane_potential, spikes)) in enumerate(
            results.items()
        ):
            # Input Current plot
            axs[i, 0].set_title(f"{label} - Input Current")
            axs[i, 0].plot(input_current)
            axs[i, 0].set_xlabel("Timesteps")
            axs[i, 0].set_ylabel("Current")

            # Membrane Potential plot
            axs[i, 1].set_title(f"{label} - Membrane Potential")
            axs[i, 1].plot(membrane_potential)
            axs[i, 1].axhline(
                y=param_sets[label].v_threshold,
                color="r",
                linestyle="--",
                label="Threshold",
            )
            axs[i, 1].axhline(
                y=0.0, color="grey", linestyle="--", label="RP"
            )
            axs[i, 1].set_xlabel("Timesteps")
            axs[i, 1].set_ylabel("Membrane Potential")
            axs[i, 1].legend(loc="upper right")

            # Add spike indicators
            spike_times = time[spikes.bool()]
            axs[i, 1].vlines(
                spike_times,
                axs[i, 1].get_ylim()[0],
                axs[i, 1].get_ylim()[1],
                color="r",
                linewidth=1,
                alpha=0.5,
            )

    plt.tight_layout()
    plt.show()
