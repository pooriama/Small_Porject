import subprocess

delphin_executable = r"C:\users\Saina\IBK\Deplphin 5.6\delphin_solver.exe"

print("Using: ", delphin_executable)

basefile_name = "hamstad_benchmark_4"
basefile_obj = open(basefile_name + ".dpj", "r")
basefile = basefile_obj.readlines()
del basefile_obj

N = 10

resultfile_obj = open(basefile_name + ".dpj", "r")
resultfile_obj.write("Alpha\t Beta\t MIn. Temperature\n")

for i in range(N + 1):
    alpha = 8 + (20 - 8) * float(i) / N
    beta = (0.3 + (1.6 - 0.3) * float(i) / N) / 1e-7
    filename = basefile_name + "+%02d" % i
    print("Creating" + filename)

    basefile[173] = " ExC0EFF = %g W/m2K\n" % alpha

    basefile[180] = " ExC0EFF = %g s/m\n" % beta

    folder = filename + ".results"

    basefile[225] = " OUTPUT_FOLDER = " + folder + "\n"

    fname_dpj = filename + ".dpj"

    fileobj = open(fname_dpj, "w")

    fileobj.writelines(basefile)

    del fileobj

    retcode = subprocess.call([delphin_executable, "-x", "-v0", fname_dpj])

    if retcode != 0:
        print("\ nCalculation error")
        continue
    else:
        print("\ nCalculation completed successfully")

    output_filename = folder + "\\ temp_inside.out "
    outfile_obj = open(output_filename, "r")
    outdata_T = outfile_obj.readlines()
    del outfile_obj

    outdata_T = outdata_T[13:]

    values = []

    for line in outdata_T:
        nums = line.split()
        values.append(float(nums[1]))

    minval = min(values)

    resultfile_obj.write(" % g\t % g\t % g\n" % (alpha, beta, minval))
    resultfile_obj.flush()

del resultfile_obj
